<script setup>
import ImageComponent from "@components/app/ImageComponent.vue";
import {defineComponent} from "vue";

const props = defineProps({
	img: {
		type: String,
		default: () => {
			return null
		}
	},
	timestamp: {
		type: String,
		default: () => {
			return "01.01.1970"
		}
	},
	title: {
		type: String,
		default: () => {
			return "No title"
		}
	},
	description: {
		type: String,
		default: () => {
			return "No desc"
		}
	},
	slug: {
		type: String,
		default: () => {
			return ''
		}
	}
})

</script>

<template>
	<router-link :to="{'name': 'news', 'params': {'newsSlug': props.slug}}" custom v-slot="{navigate}">
		<div @click="navigate" class="w-[346px] h-[516px] overflow-hidden rounded-[14px] cursor-pointer">
			<ImageComponent :img="props.img" object-fit="cover" width="100%" height="323px" radius="0" />
			<div class="mt-10px font-mulish text-light opacity-60 text-[16px] leading-[29px] p-[11px] flex gap-[4px]">
				<span>{{ props.timestamp }}</span>
			</div>
			<div class="mt-14px text-light font-manrope text-[22px] leading-[15px] p-[11px]">
				{{props.title}}
			</div>
			<div class="mt-20px text-light font-manrope opacity-70 text-[16px] leading-[26px] p-[11px]">
				<span v-html="props.description.slice(0, 40).concat('...')"></span>
			</div>
		</div>
	</router-link>
</template>