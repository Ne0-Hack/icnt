<script setup>
import HeaderComponent from "@components/app/HeaderComponent.vue";
import HtmlTextarea from "@components/app/HtmlTextarea.vue";
import {useRoute} from "vue-router";
import {onBeforeMount, reactive} from "vue";
import axios from "axios";
import LoadingSpinnerComponent from "@components/app/LoadingSpinnerComponent.vue";
import { DateTime } from "luxon";
const route = useRoute()

const state = reactive({
	loading: true,
	slug: null,
	news: {
		id: null,
		title: "",
		description: "",
		image: "",
		imageCard: ""
	},
	services: []
})

const loadNews = async () => {
	const res = await  axios.get(`${import.meta.env.backend}/contents/articles/${state.slug}`)
	if (res.status === 200) {
		state.news.id = res.data['id']
		state.news.title = res.data['title']
		state.news.description = res.data['description']
		state.news.image = res.data['image']
		state.news.author = res.data['author']
		state.news.createdAt = DateTime.fromISO(res.data['created_at'])
	}
}

const loadPage = async (slug) => {
	state.loading = true
	window.scroll({top: 0})
	state.slug = slug
	await loadNews()
	state.loading = false
}

onBeforeMount(() => {
	if (route.params['newsSlug']) {
		loadPage(route.params['newsSlug'])
	}
})

</script>

<template>
	<div v-if="state.loading" class="flex flex-col items-center justify-center">
		<LoadingSpinnerComponent />
	</div>
	<div v-else>
		<HeaderComponent :img="state.news.image">
			<template #title>{{ state.news.title }}</template>
			<template #subtitle>Публикатор: {{state.news.author}} <br>
				<b>{{state.news.createdAt.toLocaleString({month: 'long', day: 'numeric', year: 'numeric'})}}</b>
			</template>
		</HeaderComponent>
		<div class="flex flex-col  items-center mt-[70px] gap-[60px]">
			<HtmlTextarea class="w-[840px]" :html="state.news.description" />
		</div>
	</div>
</template>