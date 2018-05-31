<template>
  <div id="app">

    <!-- 顶部导航栏 -->
    <el-menu :default-active="activeIndex2" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#545c64"
      text-color="#fff" active-text-color="#ffd04b">
      <el-menu-item index="1">处理中心</el-menu-item>
      <el-submenu index="2">
        <template slot="title">我的工作台</template>
        <el-menu-item index="2-1">选项1</el-menu-item>
        <el-menu-item index="2-2">选项2</el-menu-item>
        <el-menu-item index="2-3">选项3</el-menu-item>
        <el-submenu index="2-4">
          <template slot="title">选项4</template>
          <el-menu-item index="2-4-1">选项1</el-menu-item>
          <el-menu-item index="2-4-2">选项2</el-menu-item>
          <el-menu-item index="2-4-3">选项3</el-menu-item>
        </el-submenu>
      </el-submenu>
      <el-menu-item index="3" disabled>消息中心</el-menu-item>
      <el-menu-item index="4">
        <a href="https://www.ele.me" target="_blank">订单管理</a>
      </el-menu-item>
    </el-menu>

    <!-- body轮播图 -->
    <el-carousel :interval="4000" type="card" height="200px">
      <el-carousel-item v-for="item in 6" :key="item">
        <h3>{{ item }}</h3>
      </el-carousel-item>
    </el-carousel>


    <!-- 路由 -->
    <div>开始路由</div>
    <router-link to="/">点击进入hello首页</router-link>
    <br>
    <router-link to="/book">点击进入book</router-link>
    <br>
    <br>
    <router-link to="/tag">点击进入tag</router-link>
    <br>
    <router-link to="/category">点击进入category</router-link>
    <br>
    <router-link to="/article">点击进入article</router-link>
    <br>
    <router-view></router-view>


  </div>
</template>

<script>
  export default {
    name: 'app',
    data() {
      return {
        activeIndex: '1',
        activeIndex2: '1'
      }
    },
    methods: {
      handleSelect(key, keyPath) {
        console.log(key, keyPath)
      }
    }
  }

</script>

<style>
  .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  }

  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  }

</style>
