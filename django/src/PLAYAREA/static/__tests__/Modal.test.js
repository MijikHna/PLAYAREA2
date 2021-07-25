import { mount, shallowMount } from '@vue/test-utils'

import Modal from '../components/Modal';

describe('Modal.vue', () => {
  const promiseSetter = typeof setImmediate === 'function' ? setImmediate : setTimeout;
  const flushPromises = () => {
    new Promise(promiseSetter);
  }

  let wrapper;

  

});