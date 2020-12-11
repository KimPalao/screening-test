import { mount } from '@vue/test-utils';
import ProgressOverlay from '@/components/ProgressOverlay';
import Vue from 'vue';

describe('ProgressOverlay', () => {
  it('does not have active class when value is false', async () => {
    const wrapper = mount(ProgressOverlay, {
      propsData: {
        value: false,
      }
    });
    await Vue.nextTick();
    const overlay = wrapper.getComponent({name: 'v-overlay'});
    expect(overlay.classes('v-overlay--active')).toBe(false);
  });
  it('has active class when value is false', async () => {
    const wrapper = mount(ProgressOverlay, {
      propsData: {
        value: true,
      }
    });
    const overlay = wrapper.getComponent({name: 'v-overlay'});
    expect(overlay.classes('v-overlay--active')).toBe(true);
  });
})