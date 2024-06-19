<script setup>
import OrderComponent from "@components/profile/OrderComponent.vue";
import {reactive, toRef} from "vue";

const props = defineProps({
	orders: {
		type: Array,
		default: () => {
			return []
		}
	}
})

const state = reactive({
	orders: toRef(() => props.orders)
})


</script>

<template>
	<div id="history" class="mt-[15px] p-[56px] bg-[#222222] rounded-[10px]">
		<div class="flex justify-between">
			<div class="text-yellow text-[32px] leading-[36px] font-bold uppercase">История заказов</div>
			<router-link :to="{name: 'order_review'}" tag="button">
				<button class="btn">Оставить Отзыв</button>
			</router-link>
		</div>
		<div class="mt-[44px]">
			<OrderComponent
					v-for="i in state.orders"
					:img="i.customer.img"
					:user="i.customer.firstName +' '+ i.customer.lastName"
					:service="i.service[0]"
					:category="i.service[1]"
					:deadline="i.deadline"
					:status="i.status[1]"
			/>
		</div>
	</div>

</template>