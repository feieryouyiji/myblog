<template>
  <div class="b-category-container">
    <div class="header">

    </div>
    <div class="body" v-if="items.length">
      <el-table :data="items" style="width: 100%">
        <el-table-column prop="id" label="id" width="180">
        </el-table-column>
        <el-table-column prop="name" label="名称" width="180">
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
        },
        items: []
      }
    },
    async created() {
      await this.loadItems()
    },
    methods: {
      loadItems() {
        this.$axios.get(`/api/api/v1/category/?limit=10&offset=${((this.pagination.currentPage)-1)*10}`).then(res => {
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
