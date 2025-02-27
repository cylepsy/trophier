<script setup lang="ts">
import TrophyList from '../components/TrophyList.vue'
import AddTrophy from '../components/AddTrophy.vue';
import SongList from '@/components/SongList.vue';
import {ref} from 'vue'

const childList = ref(null);
const childSongList = ref(null);

function onSubmit() {
  console.log('submitted!');
  childList.value.getTrophies();
  childSongList.value.getSongs();
}



</script>

<template>
  <main>
    <TrophyList ref="childList"/>
    <!-- <AddTrophy @submit="onSubmit"/> -->
  </main>
</template>