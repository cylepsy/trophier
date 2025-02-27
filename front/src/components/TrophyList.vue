<script lang="ts">
import axios from 'axios';
import {ref} from 'vue'
import '../assets/colors.css'

</script>
<script lang="ts" setup >
  let trophies = ref([]);
  function getTrophies() {
    console.log('getting trophies');
    const path = 'http://localhost:5000/Trophies';
    axios.get(path)
      .then((res) => {
        trophies.value = res.data.result;
        console.log('got trophies', trophies.value);
      })
      .catch((error) => {
        console.error(error);
      });
  }
  getTrophies();
  defineExpose({
    getTrophies
  })
</script>

<template>
    <!-- <div id="resp-table">
    <table>
      <tbody>
        <tr>
          <th class="header-item">Name</th>
          <th class="header-item">Rank</th>
          <th class="header-item">Description</th>
        </tr>
        <tr class="table-rows" v-for="({name, rank, description, id}, key) in trophies">
          <td>{{ name }}</td>
          <td>{{ rank }}</td>
          <td>{{ description}}</td>
        </tr>
      </tbody>
    </table>
  </div> -->

    <div class="container">
        <div class ="row">
          <div class="cell">Name</div>
          <div class="cell">Rank</div>
          <div class="cell">Description</div>
        </div>
        <div class="row" v-for="({name, rank, description, id}, key) in trophies">
          <div class="cell">{{ name }}</div>
          <div class="cell">{{ rank }}</div>
          <div class="cell">{{ description}}</div>
        </div>
  </div>

</template>

<style scoped>
table {
  border-collapse: collapse;
  width: 100%;
  table-layout: auto !important;
  word-wrap: break-word;
  background-color: var(--surface-color);
}

td {
  padding: 15px;
  text-align: center;
  color: var(--on-surface-color);
}

.header-item {
  padding: 30px 20px;
  font-size: 12px;
  text-transform: uppercase;
  background-color: var(--elv1-color);
  color: var(--on-surface-color);
}

.table-rows {
  background-color: var(--elv1-color);
}
.table-rows:nth-child(n):hover {
  background-color: var(--elv2-color);
}

.container {
  display: grid;
  grid-template-columns: 1fr; 
  grid-auto-flow: dense; 
  row-gap: 10px;
  background-color: var(--surface-color);
}
.cell {
  padding: 15px;
  text-align: center;
  color: var(--on-surface-color);
}
.row {
  display: grid;
  background-color: var(--elv1-color);
  grid-template-columns: repeat(3, 1fr); 
}
.row:nth-child(n):hover {
  background-color: var(--elv2-color);
}
</style>

