import { mount, shallowMount } from '@vue/test-utils';
import EditableRow from '@/components/EditableRow';
import Vue from 'vue';

const editable_row = {
  update: jest.fn()
}

describe('EditableRow', () => {
  it('has one column for each field plus 2', async () => {
    const wrapper = mount(EditableRow, {
      propsData: {
        value: {},
        index: 0,
        pk: 'id',
        label: 'text',
        fields: [
          {name: 'text', type: 'text'},
          {name: 'extra', type: 'extra'}
        ],
        updateUrl: ''
      },
    });
    expect(wrapper.findAll('.col')).toHaveLength(4);
  });

  const propsData = {
    value: {
      id: 1,
      text: 'text',
    },
    index: 0,
    pk: 'id',
    label: 'text',
    fields: [
      {name: 'text', type: 'text'},
    ],
    updateUrl: ''
  };

  let spy;

  it('focuses on a v-text-field when a .editable element is clicked', async () => {
    const div = document.createElement('div')
    div.id = 'root';
    document.body.appendChild(div);
    const wrapper = mount(EditableRow, {
      propsData: propsData,
      attachTo: '#root'
    });

    const editable_text = wrapper.find('[data-field="text"]');
    await editable_text.trigger('click');
    expect(wrapper.vm.$data.focused).toBe('text');
    const v_text_field_input = wrapper.getComponent({ ref: 'text'}).find('input');
    expect(v_text_field_input.element).toBe(document.activeElement);
    wrapper.destroy();
  });

  it('hides the text field on blur', async() => {
    const wrapper = mount(EditableRow, {
      propsData: propsData,
    });
    const editable_text = wrapper.find('[data-field="text"]');
    await editable_text.trigger('click');
    expect(wrapper.vm.$data.focused).toBe('text');
    const v_text_field_input = wrapper.getComponent({ ref: 'text'}).find('input');
    await v_text_field_input.trigger('blur');
    expect(wrapper.findComponent({ref: 'text'}).exists()).toBe(false);
  });

  it('hides the text field on pressing enter', async() => {
    const wrapper = mount(EditableRow, {
      propsData: propsData,
    });
    const editable_text = wrapper.find('[data-field="text"]');
    await editable_text.trigger('click');
    expect(wrapper.vm.$data.focused).toBe('text');
    const v_text_field_input = wrapper.getComponent({ ref: 'text'}).find('input');
    await v_text_field_input.trigger('keyup.enter');
    expect(wrapper.findComponent({ref: 'text'}).exists()).toBe(false);
  });
  
  it('displays a progress spinner when submitting, and hides when not', async () => {
    // spy = jest.spyOn(EditableRow.methods, 'remove');
    // const div = document.createElement('div');
    // div.id = 'root';
    // div.setAttribute('data-app', true);
    // document.body.appendChild(div);

    const wrapper = mount(EditableRow, {
      propsData: propsData,
      // attachTo: '#root'
    });

    wrapper.setData({submitting: true});
    await Vue.nextTick();
    expect(wrapper.findComponent({name: 'v-progress-circular'}).exists()).toBe(true);
    
    wrapper.setData({submitting: false});
    await Vue.nextTick();
    expect(wrapper.findComponent({name: 'v-progress-circular'}).exists()).toBe(false);

    wrapper.destroy();
  });

})