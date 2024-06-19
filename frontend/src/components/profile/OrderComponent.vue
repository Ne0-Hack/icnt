<script setup>
import ImageComponent from "@components/app/ImageComponent.vue";

const props = defineProps({
	img: {
		type: String,
		default: () => {
			return null
		}
	},
	user: {
		type: String,
		default: () => {
			return '-'
		}
	},
	service: {
		type: String,
		default: () => {
			return '-'
		}
	},
	category: {
		type: String,
		default: () => {
			return '-'
		}
	},
	deadline: {
		type: String,
		default: () => {
			return '-'
		}
	},
	status: {
		type: String,
		default: () => {
			return 'Рассматривается'
		}
	}
})

</script>

<template>
	<div class="grid grid-cols-5 font-bold leading-[36px] font-manrope h-[100px] border-y border-light items-center">
		<div class="flex gap-[10px] items-center">
			<ImageComponent :img="props.img" object-fit="cover" radius="100%" width="50px" height="50px" />
			{{ props.user }}
		</div>
		<div>
			{{ props.service }}
		</div>
		<div>
			{{ props.category }}
		</div>
		<div>
			{{ props.deadline }}
		</div>
		<div class="text-end">
			{{ props.status }}
		</div>
	</div>
</template>