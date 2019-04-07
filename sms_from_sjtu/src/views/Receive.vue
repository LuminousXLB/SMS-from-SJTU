<template>
  <div class="home">
    <h1 style="margin: 1em;">收信</h1>

    <h2 style="margin: 1em;">数据预览</h2>
    <div v-if="worksheet">
      <a-table :columns="columns" :dataSource="data" size="small" rowKey="__rowNum__" bordered/>
    </div>
  </div>
</template>

<script>
import XLSX from "xlsx";
import { mapState } from "vuex";

export default {
  name: "home",
  data() {
    return {};
  },
  computed: {
    ...mapState({
      headers: "headers",
      data: "data",
      pkey: "pkey",
      msgsent: "msgsent"
    })
  }
};
</script>
