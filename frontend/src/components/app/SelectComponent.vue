<script setup>
import {reactive, ref, toRef} from "vue";
import { onClickOutside } from '@vueuse/core'
const props = defineProps({
	placehloder: {
		type: String,
		default: () => {
			return ""
		}
	},
	width: {
		type: String,
		default: () => {
			return '400px'
		}
	},
	options: {
		type: Array,
		default: () => {
			return []
		}
	},
	optId: {
		type: String,
		default: () => {
			return 'id'
		}
	},
	optName: {
		type: String,
		default: () => {
			return 'name'
		}
	},
	value: {
		type: Number,
		default: () => {
			// null is default value
			return null
		}
	},
	name: {
		type: String,
		default: () => {
			return ''
		}
	},
	error: {
		type: Array,
		default: () => {
			return []
		}
	},
	theme: {
		type: String,
		default: () => {
			return 'dark'
		}
	},
	label: {
		type: String,
		default: () => {
			return ''
		}
	},
	disabled: {
		type: Boolean,
		default: () => {
			return false
		}
	}
})
const emits = defineEmits(["onInput"])

const state = reactive({
	value: props.value,
	error: toRef(() => props.error),
	options: toRef(() => props.options),
	active: false
})

const inputHandler = () => {
	if (state.value === null) {
		state.error.push("Выберите вариант из списка")
	} else {
		emits('onInput', state.value)
	}
}
const target = ref()
onClickOutside(target, event => state.active = false)
</script>

<template>
	<div
			class="relative"
			ref="target"
			:class="{
					'theme-dark': props.theme === 'dark',
					'theme-light': props.theme === 'light',
			}"
	>
		<label class="label"
				v-if="props.label.length > 0">
			{{ props.label }}
		</label>
		<div
				class="relative flex items-center"
				:style="{
						'width': props.width
				}"

		>
			<div
					@click.self="state.active = !state.active"
					class="select-component"
					:class="{
						'danger': state.error.length !== 0,
					}"
			>
				<span class="pointer-events-none"
							v-if="state.value === null">
					{{ props.placehloder }}
				</span>
				<span v-else>
					{{ state.options.find(e => e[props.optId] === state.value).title}}
				</span>
				<ul class="select-list"
						:class="{'active': state.active}">
					<li @click="
							state.value = el[props.optId];
							state.active = false;
							inputHandler()
							"
							class="select-item"
							v-for="el in state.options">
						{{ el[props.optName] }}
					</li>
				</ul>
			</div>

			<div class="apperance">
				<svg width="16" height="9" viewBox="0 0 16 9" fill="none" xmlns="http://www.w3.org/2000/svg">
					<path fill="black" d="M7.29289 8.70711C7.68342 9.09763 8.31658 9.09763 8.70711 8.70711L15.0711 2.34315C15.4616 1.95262 15.4616 1.31946 15.0711 0.928932C14.6805 0.538408 14.0474 0.538408 13.6569 0.928932L8 6.58579L2.34315 0.928932C1.95262 0.538408 1.31946 0.538408 0.928932 0.928932C0.538408 1.31946 0.538408 1.95262 0.928932 2.34315L7.29289 8.70711ZM7 7V8H9V7H7Z" />
				</svg>
			</div>
		</div>

		<ul v-show="state.error.length !== 0"
				 class="text-danger mt-[3px] absolute top-[100%]"
		>
			<li v-for="val of state.error">
				{{ val }}
			</li>
		</ul>
	</div>
</template>

<style scoped>
	.select-component {
		@apply flex rounded-[8px] outline-none border-[1px] border-[transparent] w-full h-[50px] px-[20px]
		font-manrope transition-colors appearance-none items-center text-[16px] leading-[28px] select-none
	}

	.select-list {
		@apply hidden flex-col absolute z-20 top-[90%] left-0 w-full px-[20px] py-[18px] gap-[14px] rounded-b-[8px]
	}

	.select-list.active {
		@apply flex
	}

	.select-item {
		@apply text-[16px] leading-[28px] cursor-pointer
	}

	.select-item:hover {
		@apply text-yellow
	}

	.select-component:disabled {
		@apply cursor-not-allowed
	}

	.apperance {
		@apply absolute right-[20px] pointer-events-none cursor-pointer
	}

	.theme-dark .apperance > svg > path {
		fill: #FFFFFF;
	}

	.theme-light .apperance > svg > path {
		fill: #000000;
	}

	.label {
		@apply block font-raleway text-[18px] leading-[32px] font-medium
	}

	.theme-dark .select-component {
		@apply bg-[#141414] text-light;
		color-scheme: dark;
	}
	.theme-dark .select-component::placeholder {
		@apply opacity-50
	}
	.theme-dark > .label {
		@apply text-light
	}

	.theme-dark .select-list {
		@apply bg-[#141414] text-light;
	}

	.theme-light .select-component {
		@apply bg-[#FFFFFF] text-dark border-dark border-opacity-[12%]
	}
	.theme-light .select-component::placeholder {
		@apply text-dark opacity-50
	}
	.theme-light > .label {
		@apply text-dark
	}

	.select-component:focus {
		@apply border-yellow bg-opacity-10 caret-yellow;
		box-shadow: 0 0 30px 0 #BCFF0026;

	}
	.select-component.danger {
		@apply border-danger
	}
</style>