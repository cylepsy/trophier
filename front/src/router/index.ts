import { createRouter, createWebHistory } from 'vue-router'
import SongView from '../views/SongView.vue'
import TemplateView from '../views/TemplateView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/songview',
      name: 'songview',
      component: SongView,
    },
    {
      path:'/tempview',
      name: 'tempview',
      component: TemplateView,
    }
  ],
})

export default router
