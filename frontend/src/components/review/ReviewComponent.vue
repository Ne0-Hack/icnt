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
	userName: {
		type: String,
		default: () => {
			return "No user"
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
	}
})

</script>

<template>
	<div class="w-[342px] h-[418px] font-manrope text-center flex flex-col items-center">
		<ImageComponent class="relative top-[50px] flex-shrink-0" :img="props.img" :object-fit="true" width="100px" height="100px" radius="100%" />
		<div class="bg-[#141414] pt-[50px] pb-[20px] w-full rounded-[8px]">
			<div class="text-[18px] mt-[15px]">
				{{props.userName}}
			</div>
			<div class="text-yellow text-[20px] leading-[25px] mt-[20px]">
				{{props.title}}
			</div>
			<div class="text-[14px] leading-[26px] p-[11px] h-[130px] mt-[10px] flex-shrink">
				<span v-html="props.description.slice(0, 250)"></span>
			</div>
			<div class="mt-[10px] font-mulish">
				<span>{{ props.timestamp }}</span>
			</div>
		</div>
	</div>
</template>