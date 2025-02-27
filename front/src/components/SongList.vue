<script lang="ts" >
import axios from 'axios';
import { ref } from 'vue';
</script>

<script lang="ts" setup>
let songs = ref([]);

function getSongs() {
  const path = 'http://localhost:5000/Songs';
  axios.get(path)
    .then((res) => {
      songs.value = res.data.result;
    })
    .catch((error) => {
      console.error(error);
    });
}
getSongs();
defineExpose({
  getSongs
});
</script>

<template>

  <div id="resp-table">
    <table>
      <tbody>
      <tr>
          <th class="header-item">Title</th>
          <th class="header-item">Artist</th>
          <th class="header-item">Genre</th>
          <th class="header-item">Type</th>
          <th class="header-item">Instrument</th>
        </tr>
        <tr class="table-rows" v-for="({title, artist, genre, type, instrument, id}, key) in songs">
          <td>{{ title }}</td>
          <td>{{ artist }}</td>
          <td>{{ genre }}</td>
          <td>{{ type }}</td>
          <td>{{ instrument }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
table {
  border-collapse: collapse;
  width: 100%;
  table-layout: auto !important;
  word-wrap: break-word;
}

td {
  padding: 24px;
  text-align: center;
  border-bottom: 1px solid rgb(224, 242, 237);
}

.header-item {
  padding: 30px 20px;
  font-size: 12px;
  background-color: rgb(224, 242, 237);
  text-transform: uppercase;
}

.table-rows:nth-child(odd) {
  background-color: rgb(250, 250, 250);
}

.table-rows:nth-child(n):hover {
  background-color: rgb(244, 246, 245);
}
</style> 

