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

  <div class="table-wrapper">
    <div  class="row" v-for="({title, artist, genre, type, instrument, id}, key) in songs">
      <div class="title-cell">
        <div class="cell title-text">{{ title }}</div>
        <div class="cell artist-text"> {{ artist }}</div>
      </div>
      <div class="cell">{{ genre }}</div>
      <div class="cell">{{ type }}</div>
      <div class="cell">{{ instrument }}</div>
    </div>
  </div>
</template>

<style scoped>
.table-wrapper {
  display: grid;
  gap: 20px;
  background-color: var(--surface-color);
  padding-left: 5%;
  padding-right: 5%;
  padding-top: 5%;
  padding-bottom: 5%;
}
.row {
  display: grid;
  grid-template-columns: 3fr 1fr 1fr 1fr;
  grid-template-rows: auto;
  border-radius: 12px;
  background-color: var(--surface-container-color);
}
.row:nth-child(n):hover {
  background-color: var(--elv2-color);
}
.cell {
  padding: 30px;
  text-align: left;
  color: var(--on-surface-color);
  font-family: Roboto;
  font-size: var(--body-font-size);
  font-weight: var(--body-font-weight);
}
.title-text {
  color: var(--on-surface-color);
  font-family: Roboto;
  font-size: var(--title-font-size);
  font-weight: var(--title-font-weight);
  padding-bottom: 5px;
}
.artist-text {
  color: var(--on-surface-varient-color);
  font-family: Roboto;
  font-size: var(--body-small-font-size);
}
</style>
