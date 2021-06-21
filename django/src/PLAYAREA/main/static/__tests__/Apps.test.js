import { mount } from '@vue/test-utils';

import Apps from '../components/Apps.vue';
import AppCard from '../components/AppCard';
import { config } from '../js/config';

describe('Apps.vue', () => {
  const flushPromises = () =>
    new Promise(typeof setImmediate === 'function' ? setImmediate : setTimeout);

  let wrapper;
  window.fetch = jest.fn();

  beforeEach(() => {
    jest.clearAllMocks();
    jest.clearAllTimers();
  });

  afterEach(() => {
    wrapper.destroy();
  });

  test('Apps Component is instantiated', async () => {
    // Arrange
    window.fetch.mockResolvedValueOnce({
      status: 200,
      json: () => Promise.resolve([]),
    });

    // Act
    wrapper = await mount(Apps);
    await flushPromises();

    // Assert
    expect(wrapper.vm).toBeTruthy();
  });

  test('Apps Component fetches the Apps', async () => {
    // Arrange

    window.fetch.mockResolvedValueOnce({
      status: 200,
      json: () =>
        Promise.resolve([
          {
            'name': 'testApp',
            'href': 'testAppHref',
            'subApps': undefined,
          },
        ]),
    });

    // Act
    wrapper = await mount(Apps);
    await flushPromises();

    // Assert
    expect(wrapper.vm).toBeTruthy();
    expect(fetch).toHaveBeenCalledTimes(1);

    expect(fetch).toHaveBeenLastCalledWith(config.urls.allApps, {
      method: 'GET',
      mode: 'cors',
      cache: 'no-cache',
      credentials: 'same-origin',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    expect(wrapper.vm.apps.length).toEqual(1);
    expect(wrapper.findAllComponents(AppCard).length).toBe(1);
  });
});
