<script lang="ts">
import axios from 'axios';
import {ref} from 'vue'
</script>

<script lang="ts" setup>

let addType = ref('trophy');

let addTrophyForm = ref({
  name:'',
  rank:0,
  desc:''
});

let addSongForm = ref(
  [
    {name: 'title',value: ''},
    {name: 'artist',value: ''},
    {name: 'instrument',value: ''},
    {name: 'type',value: ''},
    {name: 'genre',value: ''},
    {name: 'tag1',value: ''},
  ]
);

const emit = defineEmits(['submit']);
function postData(payload:object) {
  const path = 'http://localhost:5000/' + 'Add'+ addType.value;
  axios.post(path, payload)
    .then(() => {
      emit('submit');
    })
    .catch((error) => {
      console.error(error);
    });
};

function initForm() {
  addTrophyForm.value.name = '';
  addTrophyForm.value.rank = 0;
  addTrophyForm.value.desc = '';

  addSongForm.value[0].value = '';
  addSongForm.value[1].value = '';
  addSongForm.value[2].value = '';
  addSongForm.value[3].value = '';
  addSongForm.value[4].value = '';
  addSongForm.value[5].value = '';
};

function handleAddSubmit() {
  if (addType.value == 'trophy') {
    const payload = {
      name: addTrophyForm.value.name,
      rank: addTrophyForm.value.rank,
      desc: addTrophyForm.value.desc,
    };
    postData(payload);
    initForm();
  }
  if (addType.value == 'song') {
    const payload = {
      title : addSongForm.value[0].value,
      artist : addSongForm.value[1].value,
      instrument: addSongForm.value[2].value,
      type: addSongForm.value[3].value,
      genre: addSongForm.value[4].value,
      tag: addSongForm.value[5].value,
    };
    postData(payload);
    initForm();
  }
};


</script>

<template>
  <!-- Type Select Box -->
  <select name="addtype" v-model="addType">
    <option value="trophy">Trophy</option>
    <option value="song">Song</option>
  </select>

  <!-- Add Trophy Form -->
  <div v-if="addType == 'trophy'" id="trophyForm">
    <form>
    <label for="name">name:</label><br>
    <input type="text" class="nameInput" v-model="addTrophyForm.name"><br>
    <label for="rank">rank:</label><br>
    <select name="rank" v-model="addTrophyForm.rank">
      <option value="0">Bronze</option>
      <option value="1">Silver</option>
      <option value="2">Gold</option>
      <option value="3">Platinum</option>
    </select>
    <br>
    <label for="desc">Description:</label><br>
    <input type="text" class="descInput" v-model="addTrophyForm.desc">
    </form>
   <d-button @click=handleAddSubmit>Add Trophy</d-button>
  </div>

  <!-- Add Song Form -->
  <div v-if="addType == 'song'" id="songForm">
    <form>
      <div v-for="song in addSongForm">
        <p >{{ song.name }}
        <br>
        <input type="text" class="nameInput" v-model="song.value"><br>
        </p>
      </div>
    </form>
    <d-button @click=handleAddSubmit>Add Song</d-button>
  </div>
</template>

<style scoped>
.nameInput {
  width: 200px;
}
.descInput {
  width: 800px;
}
</style>
