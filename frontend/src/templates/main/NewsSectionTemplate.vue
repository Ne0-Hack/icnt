<script setup>
import SliderComponent from "@components/main/SliderComponent.vue";
import NewsLinkComponent from "@components/news/NewsLinkComponent.vue";
import {onBeforeMount, reactive} from "vue";
import axios from "axios";
import {DateTime} from "luxon";
import SectionComponent from "@components/main/SectionComponent.vue";

const state = reactive({
	news: []
})

const loadNews = async () => {
	const res = await  axios.get(`${import.meta.env.VITE_API_ENDPOINT}/contents/articles`)
	if (res.status === 200) {
		state.news = []
		for (let el of res.data) {
			state.news.push({
				"title": el['title'],
				"img": el['image'],
				"tag": 'empty',
				"description": el['description'],
				"slug": el['slug'],
				"timestamp": DateTime.fromISO(el['created_at']).toLocaleString({month: 'numeric', day: 'numeric', year: 'numeric'}),
			})
		}
	}
}

onBeforeMount(async () => {
	await loadNews()
})

</script>

<template>
	<SliderComponent v-if="state.news.length > 0" id="news-list" :between="17" :per-view="4" :slide-component="NewsLinkComponent" :slide-data="state.news">
		<template #title>Блог новостей</template>
	</SliderComponent>
	<SectionComponent v-else>
		<template #title>Блог новостей</template>
		<template #content><div class="text-[24px] text-center">Новостей нет</div></template>
	</SectionComponent>
</template>