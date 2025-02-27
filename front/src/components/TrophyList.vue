<script lang="ts">
import axios from 'axios';
import {ref, computed} from 'vue'
import '../assets/colors.css'

</script>
<script lang="ts" setup >
  let trophies = ref([]);
  let trophyEntry = ref([])

  function getData(songid:number) {
    console.log('getting trophies');

    // Get Trophy Data
    const path = 'http://localhost:5000/Trophies'; axios.get(path)
      .then((res) => {
        trophies.value = res.data.result;
        console.log('got trophies', trophies.value);
      })
      .catch((error) => {
        console.error(error);
      });
    
    // Get Trophy Entries
    const entryPath = 'http://localhost:5000/querysong';
    const payload = {
      songid: songid,
    };
    axios.post(entryPath, payload)
      .then((res) => {
        trophyEntry.value = res.data.result;
        console.log(trophyEntry);
      })
      .catch((error) => {
        console.error(error);
      });
  }

  getData(1);
  defineExpose({
    getTrophies: getData
  })

  function rankLevel(rank:number) {
    switch (rank) {
      case 0:
        return 'Bronze';
        break;
      case 1:
        return 'Silver';
        break;
      case 2:
        return 'Gold';
        break;
      case 3:
        return 'Platinum';
        break;
      default:
        break;
    }
  };

  function isTrophyEarned(trophyid:number) {
    if (trophyEntry.value.some((trophy)=>{
      return trophy.id == trophyid;
    }))
      return 'Earned';
    else
      return 'Not Earned';
  }

  
</script>

<template>
    <div class="table-wrapper">
        <div class="row" v-for="({name, rank, description, id}, key) in trophies">
          <div class="cell">{{ isTrophyEarned(id) }}</div>
          <div class="title-cell">
            <div class="cell title-text">{{ name }}</div>
            <div class="cell trophy-text">{{ rankLevel(rank) }}</div>
          </div>
          <div class="cell">{{ description}}</div>
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
  grid-template-columns: 1fr 4fr 7fr;
  grid-template-rows: auto;
  grid-template-areas: "cell cell cell";
  border-radius: 12px;
  background-color: var(--surface-container-color);
}
.row:nth-child(n):hover {
  background-color: var(--elv2-color);
}
.cell {
  padding: 20px;
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
.trophy-text {
  color: var(--on-surface-varient-color);
  font-family: Roboto;
  font-size: var(--body-small-font-size);
}
</style>

