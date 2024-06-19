<script setup>
	import ImageComponent from "@components/app/ImageComponent.vue";
	import {ref} from "vue";
	import axios from "axios";

	const props = defineProps({
		img: {
			type: String,
			default: () => {
				return ''
			}
		},
		user_id: {
			type: String,
			default: () => {
				return ''
			}
		}
	})

	const emits = defineEmits(['refresh'])

	const file = ref();
	const onFileChange = (ev) => {
		const target = ev.target
		if (target && target.files) {
			file.value = target.files[0]
			uploadImage(file.value)
		}
	}



	const uploadImage = (file) => {
		axios.putForm(`http://127.0.0.1:8000/users/${props.user_id}/`, {
			'image': file
		})
				.then(e => {
					emits("refresh")
				})
	}

</script>

<template>
	<div class="w-[246px] h-[246px] relative">
		<ImageComponent :img="props.img" object-fit="cover" width="246px" height="246px" radius="100%" />
		<input
				class="absolute top-0 left-0 w-full h-[246px] opacity-0 cursor-pointer"
				type="file"
				@change="onFileChange"
				accept="image/*"
		>
	</div>
</template>