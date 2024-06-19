<script setup>
import ImageComponent from "@components/app/ImageComponent.vue";
const props = defineProps({
	img: {
		type: String,
		default: () => {
			return null
		}
	},
	title: {
		type: String,
		default: () => {
			return "No text"
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

<template >
	<router-link :to="{'name': 'service', 'params': {'serviceSlug': props.slug}}" custom v-slot="{navigate}">
		<div @click="navigate" class="flex flex-col w-[388px] cursor-pointer">
			<ImageComponent :img="props.img" width="100%" height="463px" object-fit="cover" radius="14px" />
			<div class="flex mt-[25px] items-center uppercase gap-3 text-light font-semibold text-[18px]">
				{{props.title}}
				<svg width="16" height="15" viewBox="0 0 16 15" fill="none" xmlns="http://www.w3.org/2000/svg">
					<path d="M15.3966 1C15.3966 0.444433 14.9516 -0.00594248 14.4026 -0.00594276L5.45639 -0.00594234C4.90741 -0.0059427 4.46237 0.444433 4.46237 1C4.46237 1.55557 4.90741 2.00594 5.45639 2.00594L13.4086 2.00594L13.4086 10.0535C13.4086 10.609 13.8536 11.0594 14.4026 11.0594C14.9516 11.0594 15.3966 10.609 15.3966 10.0535L15.3966 1ZM2.25952 14.7113L15.1055 1.71131L13.6997 0.288691L0.853761 13.2887L2.25952 14.7113Z" fill="white"/>
				</svg>
			</div>
		</div>
	</router-link>
</template>