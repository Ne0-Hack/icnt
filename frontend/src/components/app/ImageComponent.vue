<script setup>
import no_photo from "@images/no_photo.svg"
import {onBeforeMount, onMounted, reactive, toRef} from "vue";
import axios from "axios";

const props = defineProps({
	img: {
		type: String,
		default: () => {
			return null
		},
	},
	width: {
		type: String,
		default: () => {
			return 'auto'
		}
	},
	height: {
		type: String,
		default: () => {
			return 'auto'
		}
	},
	objectFit: {
		type: String,
		default: () => {
			return 'contain'
		}
	},
	blackout: {
		type: Boolean,
		default: () => {
			return false
		}
	},
	radius: {
		type: String,
		default: () => {
			return '0'
		}
	},
	padding: {
		type: Number,
		default: () => {
			return 14
		}
	},
	background: {
		type: Boolean,
		default: () => {
			return false
		}
	}
})

const state = reactive({
	img: toRef(() => props.img),
	no_image: false,
	objectFit: props.objectFit
})

const styleContainer ={
	'width': props.width,
	'height': props.height,
	'border-radius': props.radius,
	'background': props.background ? 'rgb(26, 26, 26)' : ''
}

const styleImg = {
	'object-fit': props.objectFit,
	'opacity': props.blackout ? '0.2' : '1'
}

onMounted(async () => {
	// try {
	// 	const request = await axios.get(state.img)
	// 	console.log(request.status)
	// 	if (request.status !== 200) {
	// 		state.no_image = true
	// 	} else if (state.img.length <= 0) {
	// 		state.no_image = true
	// 	}
	// } catch (e) {
	// 	console.log(e)
	// }
})

</script>

<template>
	<div class="img-container"
			 :style="styleContainer">
		<img :src="state.no_image ? no_photo : state.img"
				 :style="styleImg"
				 alt="">
	</div>

</template>
<style>

.img-container {
	overflow: hidden;
}

.img-container > img {
	padding: 0;
	margin: 0;
	width: 100%;
	height: 100%;
}

</style>