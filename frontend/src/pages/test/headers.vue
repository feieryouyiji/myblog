
<template>
  <div id="app"> I am headers

      <VueUEditor></VueUEditor>
  </div>

</template>
<script>
  import VueUEditor from 'vue-ueditor'
  console.log(VueUEditor, 'VueUEditor')
  export default {
    name: 'headers',
    data () {
      return {

      }
    },
    components: {
      VueUEditor,
    },
    created(){
      console.log('加载了')
    },
    methods: {

    }
  }
</script>

<style>

</style>
