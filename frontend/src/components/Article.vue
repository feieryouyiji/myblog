<template>
  <div class="b-article-container">
    <div class="header">

    </div>
    <div class="body" v-if="items.length">
      <el-table :data="items" style="width: 100%">
        <el-table-column prop="id" label="id" width="180">
        </el-table-column>
        <el-table-column prop="created_time" label="创建时间" width="180">
        </el-table-column>
        <el-table-column prop="modify_time" label="修改时间" width="180">
        </el-table-column>
        <el-table-column prop="title" label="文章标题" width="180">
        </el-table-column>
        <el-table-column prop="author" label="作者" width="180">
        </el-table-column>
        <el-table-column prop="is_publish" label="是否发布" width="180">
        </el-table-column>
      </el-table>
    </div>
    <div class="footer">
      <el-pagination :current-page="pagination.currentPage" @current-change="hanldePageChange" background layout="prev, pager, next"
        :total="pagination.total_count">
      </el-pagination>
    </div>

  </div>
</template>

<script>
  export default {
    data() {
      return {
        pagination: {
          total_count: 0,
          currentPage: 1
        },
        items: []
      }
    },
    async created() {
      await this.loadItems()
      this.test()
    },
    methods: {
      async test() {
        const res = await this.$axios.get('/api/api/v1/article/')
        console.log(res, 'res<==test')
      },
      loadItems() {
        this.$axios.get(`/api/api/v1/article/?limit=10&offset=${((this.pagination.currentPage)-1)*10}`).then(res => {
          console.log(res)
          this.items = res.data.objects
          this.pagination.total_count = res.data.meta.total_count
        })
      },
      async hanldePageChange(page) {
        this.pagination.currentPage = page
        this.loadItems()
      },
    }
  }

</script>
