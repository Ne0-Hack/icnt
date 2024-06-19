<script setup>
import SectionComponent from "@components/main/SectionComponent.vue";
import WorkLinkComponent from "@components/work/WorkLinkComponent.vue";
import {onBeforeMount, reactive} from "vue";
import axios from "axios";

const state = reactive({
	works: []
})

const loadWorks = async () => {
	const res = await  axios.get("http://127.0.0.1:8000/contents/works/?l=4")
	if (res.status === 200) {
		state.works = res.data
	}
}

onBeforeMount(async () => {
	await loadWorks()
})

</script>

<template>
	<SectionComponent id="works-list">
		<template #title>Наши работы</template>
		<template #content>
			<div class="flex justify-between gap-[70px] flex-wrap">
				<WorkLinkComponent v-for="work in state.works" :img="work.imageA" :tags="work.tags"></WorkLinkComponent>
			</div>
		</template>
		<template #footer>
			<router-link :to="{name: 'works'}" class="text-light border-light inline-flex border rounded-[50px] px-[22px] py-[11px] font-semibold font-urbanist text-[16px] leading-[23.8px] cursor-pointer">
				Посмотреть все проекты
			</router-link>
		</template>
	</SectionComponent>

</template>