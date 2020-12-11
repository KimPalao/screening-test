import Vuetify from 'vuetify';
import { mount } from '@vue/test-utils';
import axios from 'axios';
import HomeList from '@/components/HomeList.vue';
import { values } from './values';
import { principles } from './principles';
import flushPromises from 'flush-promises';

jest.mock('axios');
axios.get.mockImplementation((url) => {
  switch (url) {
    case `${process.env.VUE_APP_BACKEND_URL}/api/values`:
      return Promise.resolve({data: values})
    case `${process.env.VUE_APP_BACKEND_URL}/api/principles`:
      return Promise.resolve({data: principles})
    default:
      return Promise.reject(new Error('not found'))
  }
})

describe('HomeList', () => {
  it('renders two lists and 16 list items', async () => {
    const wrapper = mount(HomeList);
    expect(wrapper.findAll('ol')).toHaveLength(2);
    await flushPromises();
    expect(wrapper.findAll('li')).toHaveLength(16);
  })
})