<script setup>
import SectionComponent from "@components/main/SectionComponent.vue";
import ServiceLinkComponent from "@components/service/ServiceLinkComponent.vue";
import {onBeforeMount, reactive} from "vue";
import axios from "axios";

const state = reactive({
	services: []
})

const loadServices = async () => {
	const res = await  axios.get(`${import.meta.env.VITE_API_ENDPOINT}/services/service/?l=3`)
	if (res.status === 200) {
		state.services = res.data
	}
}

onBeforeMount(async () => {
	await loadServices()
})

</script>

<template>
	<SectionComponent id="services-list">
		<template #title>Наши услуги</template>
		<template #content>
			<div class="flex justify-between gap-[42px]">
				<ServiceLinkComponent  v-for="(val, key) in state.services" :slug="val['slug']" :title="val['title']" :img="val['image_card']"></ServiceLinkComponent>
			</div>
		</template>
	</SectionComponent>
</template>