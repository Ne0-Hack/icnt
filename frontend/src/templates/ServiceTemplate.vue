<script setup>
import HeaderComponent from "@components/app/HeaderComponent.vue";
import ImageComponent from "@components/app/ImageComponent.vue";
import SectionComponent from "@components/main/SectionComponent.vue";
import ServiceLinkComponent from "@components/service/ServiceLinkComponent.vue";
import {onBeforeRouteUpdate, useRoute} from "vue-router";
import {onBeforeMount, reactive} from "vue";
import axios from "axios";
import LoadingSpinnerComponent from "@components/app/LoadingSpinnerComponent.vue";
import HtmlTextarea from "@components/app/HtmlTextarea.vue";

const route = useRoute()

const state = reactive({
	loading: true,
	slug: null,
	service: {
		id: null,
		title: "",
		description: "",
		image: "",
		imageCard: ""
	},
	services: []
})

const loadService = async () => {
	const res = await  axios.get(`${import.meta.env.VITE_API_ENDPOINT}/services/service/${state.slug}`)
	if (res.status === 200) {
		state.service.id = res.data['id']
		state.service.title = res.data['title']
		state.service.description = res.data['description']
		state.service.image = res.data['image']
		state.service.imageCard = res.data['image_card']
	}
}

const loadServices = async () => {
	const res = await  axios.get(`${import.meta.env.VITE_API_ENDPOINT}/services/service/?l=2&e=${state.service.id}`)
	if (res.status === 200) {
		state.services = res.data
	}
}


const loadPage = async (slug) => {
	state.loading = true
	state.slug = slug
	await loadService()
	await loadServices()
	state.loading = false
}

onBeforeMount(() => {
	if (route.params['serviceSlug']) {
		loadPage(route.params['serviceSlug'])
	}
})

onBeforeRouteUpdate(async () => {
	if (route.params['serviceSlug']) {
		await loadPage(route.params['serviceSlug'])
	}
})
</script>

<template>
	<div v-if="state.loading" class="flex flex-col items-center justify-center">
		<LoadingSpinnerComponent />
	</div>
	<div v-else>
		<HeaderComponent :img="state.service.image">
			<template #title>{{ state.service.title }}</template>
		</HeaderComponent>
		<div class="container flex mt-[70px] gap-[60px]">
			<div class="flex w-full flex-col gap-[45px]">
				<HtmlTextarea :html="state.service.description" />
			</div>
			<div class="flex-shrink-0">
				<ImageComponent :img="state.service.imageCard" width="568px" height="654px" object-fit="cover" radius="10px" />
			</div>
		</div>
		<SectionComponent>
			<template #title><span class="block text-center">Другие услуги</span></template>
			<template #content>
				<div class="flex justify-between">
						<ServiceLinkComponent v-for="val in state.services" :slug="val['slug']" :title="val['title']" :img="val['image_card']"></ServiceLinkComponent>
				</div>
			</template>
		</SectionComponent>
	</div>
</template>


