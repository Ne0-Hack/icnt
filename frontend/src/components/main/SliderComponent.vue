<script setup>
import 'swiper/css';
import 'swiper/css/pagination';

import {reactive, ref} from "vue";
import {Swiper, SwiperSlide} from 'swiper/vue';
import {Pagination} from "swiper/modules";

import SectionComponent from "@components/main/SectionComponent.vue";
import ServiceLinkComponent from "@components/service/ServiceLinkComponent.vue";

const props = defineProps({
	slideComponent: {
		type: String,
		required: true
	},
	slideData: {
		type: Array,
		default: () => {
			return []
		}
	},
	between: {
		type: Number,
		default: () => {
			return 5
		}
	},
	perView: {
		type: Number,
		default: () => {
			return 3
		}
	},
	shadowBorders: {
		type: Boolean,
		default: () => {
			return false
		}
	}
})




const state = reactive({
	swiper: ref()

})

const onSwiper = (el) => {
	state.swiper = el
}


</script>

<template>
	<SectionComponent>
		<template #title>
			<slot name="title"></slot>
		</template>
		<template #header>
			<div class="flex gap-[15px] items-end justify-center">
				<div @click="state.swiper.slidePrev()"
								class="flex items-center justify-center cursor-pointer rounded-[50%] w-[27px] h-[27px] border border-light">
					<svg width="15" height="8" viewBox="0 0 15 8" fill="none" xmlns="http://www.w3.org/2000/svg">
						<path d="M14.4452 3.80298L1.2207 3.80298" stroke="white"/>
						<path d="M4.08582 6.88892L1.0001 3.8032L4.08582 0.717487" stroke="white"/>
					</svg>
				</div>
				<div @click="state.swiper.slideNext()"
								class="flex items-center justify-center cursor-pointer rounded-[50%] w-[27px] h-[27px] border border-light">
					<svg width="15" height="8" viewBox="0 0 15 8" fill="none" xmlns="http://www.w3.org/2000/svg">
						<path d="M0 3.80322H13.2245" stroke="white"/>
						<path d="M10.3594 0.717285L13.4451 3.803L10.3594 6.88871" stroke="white"/>
					</svg>
				</div>
			</div>
		</template>
		<template #content>
			<Swiper
					:modules="[Pagination]"
					:slides-per-view="props.perView"
					:space-between="props.between"
					loop
					:slide
					@swiper="onSwiper"
					class="select-none"
			>
				<SwiperSlide v-for="el in props.slideData" style="width: auto">
					<component :is="props.slideComponent" v-bind="el"></component>
				</SwiperSlide>
			</Swiper>
		</template>
		<template #footer>
			<div v-if="state.swiper" class="flex gap-[6px] items-center justify-center">
				<div v-for="(val, e) of state.swiper.slides"
						 :class="{'pagination-bullet-active': e === state.swiper.activeIndex}"
						 class="pagination-bullet"
						 >
				</div>
			</div>
		</template>
	</SectionComponent>
</template>

<style>
	.pagination-bullet-active {
		opacity: 1!important;
	}
	.pagination-bullet {
		@apply bg-light opacity-70 rounded-full w-[7px] h-[7px];
	}
</style>