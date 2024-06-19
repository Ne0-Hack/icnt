<script setup>
import SliderComponent from "@components/main/SliderComponent.vue";
import ReviewComponent from "@components/review/ReviewComponent.vue";
import {onBeforeMount, reactive} from "vue";
import axios from "axios";
import {DateTime} from "luxon";
import SectionComponent from "@components/main/SectionComponent.vue";

const state = reactive({
	reviews: []
})

const loadNews = async () => {
	const res = await  axios.get(`${import.meta.env.backend}/contents/reviews`)
	if (res.status === 200) {
		state.reviews = []
		for (let el of res.data) {
			state.reviews.push({
				"title": el['title'],
				"userName": `${el['user'].last_name} ${el['user'].first_name}`,
				"img": el['user']['user_photo'],
				"description": el['text'],
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
	<SliderComponent v-if="state.reviews.length > 0" id="reviews-list" :between="17" :per-view="4" :slide-component="ReviewComponent" :slide-data="state.reviews">
		<template #title>Отзывы</template>
	</SliderComponent>
	<SectionComponent v-else>
		<template #title>Отзывы</template>
		<template #content><div class="text-[24px] text-center">Отзывов нет</div></template>
	</SectionComponent>
</template>