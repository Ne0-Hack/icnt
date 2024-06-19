<script setup>
const props = defineProps({
	login: {
		type: String,
		default: () => {
			return ''
		}
	},
	firstName: {
		type: String,
		default: () => {
			return ''
		}
	},
	lastName: {
		type: String,
		default: () => {
			return ''
		}
	},
	age: {
		type: Number,
		default: () => {
			return 0
		}
	},
	country: {
		type: String,
		default: () => {
			return ''
		}
	},
	email: {
		type: String,
		default: () => {
			return ''
		}
	},
	phone: {
		type: String,
		default: () => {
			return ''
		}
	},

})
</script>

<template>
	<div class="flex flex-col">
		<div class="text-yellow text-[32px] leading-[36px] font-bold">#{{props.login}}</div>
		<ul class="list">
			<li>
				<span>Имя:</span>
				<span>{{ props.firstName }}</span>
			</li>
			<li>
				<span>Фамилия:</span>
				<span>{{ props.lastName }}</span>
			</li>
			<li>
				<span>Возраст:</span>
				<span>{{ props.age }}</span>
			</li>
			<li>
				<span>Страна:</span>
				<span>{{ props.country }}</span>
			</li>
			<li>
				<span>Почта:</span>
				<span>{{ props.email }}</span>
			</li>
			<li>
				<span>Номер:</span>
				<span>{{ props.phone }}</span>
			</li>
		</ul>
	</div>
</template>

<style>
.list {
	@apply grid grid-cols-2 grid-rows-4 gap-x-[100px] gap-y-[12px] grid-flow-col mt-[34px]
}

.list > li {
	@apply flex justify-between text-[20px] font-manrope leading-[20px] font-bold border-b pb-[7px] w-[390px];
	border-color: rgba(188, 255, 0, 0.60);
}

</style>