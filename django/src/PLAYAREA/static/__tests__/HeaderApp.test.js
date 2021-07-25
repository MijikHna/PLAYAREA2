import { mount, shallowMount } from '@vue/test-utils'

import HeaderApp from '../components/HeaderApp';

describe('HeaderApp.vue', () => {
  const promiseSetter = typeof setImmediate === 'function' ? setImmediate : setTimeout;
  const flushPromises = () => {
    new Promise(promiseSetter);
  }

  const parentComponent = {
    $el: {
      dataset: {
        name: 'TestDataName',
        stringified: 'TestDataStringigied',
        href: 'TestDataHref',
        class: 'TestDataClass',
      }
    }
  };
  
  const parentEl = document.createElement('div');
  parentEl.dataset.name = 'TestName'
  parentEl.dataset.stringified = 'TestStringified';
  parentEl.dataset.href = 'TestHref';
  parentEl.dataset.class = 'TestClass';  

  let wrapper;

  beforeEach(() => {
    jest.resetAllMocks();
    jest.clearAllTimers();
  });

  afterEach(()=> {
    wrapper.destroy();
  });

  test('HeaderApp is instantiated', () => {
    // Arrange
    const beforeMountSpy = jest.spyOn(HeaderApp, 'beforeMount');

    // Act
    wrapper = shallowMount(HeaderApp, {
      attachTo: parentEl,  
    });

    // Assert
    expect(wrapper.vm).toBeTruthy();
    expect(beforeMountSpy).toHaveBeenCalledTimes(1);
    expect(wrapper.vm.appName).toEqual(parentEl.dataset.name);
    expect(wrapper.vm.appStringified).toEqual(parentEl.dataset.stringified);
    expect(wrapper.vm.appHref).toEqual(parentEl.dataset.href);
    expect(wrapper.vm.appClass).toEqual(parentEl.dataset.class);
  });
});