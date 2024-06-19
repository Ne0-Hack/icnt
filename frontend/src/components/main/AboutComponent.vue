<script setup>
import ImageComponent from "@components/app/ImageComponent.vue";
import AboutImageFirst from "@images/about_1.png"
import AboutImageSecond from "@images/about_2.png"

const counter = [
	{count: 15, text: "участников в команде"},
	{count: 7, text: "готовых проектов"},
	{count: 2, text: "проекта в работе"},
]
</script>

<template>
	<div class="flex flex-col gap-[30px]">
		<div class="flex gap-[56px] items-center">
			<ImageComponent :img="AboutImageFirst" width="600px" height="307px" radius="10px" object-fit="cover" class="flex-shrink-0"/>
			<div class="flex flex-col gap-[16px]">
				<div class="font-bold text-[36px] leading-[48px] tracking-[-2px]">
					Команда профессионалов
				</div>
				<div class="font-manrope text-[16px] leading-[20.8px] tracking-[2%]">
					Наши студенты и преподаватели активно занимаются исследованиями, создавая инновации, которые могут изменить
					мир! Вместе с тем, мы готовы проводить различной сложности точечные исследования вашей индустрии и предлагать
					дополнительные услуги.
				</div>
			</div>
		</div>
		<div class="flex gap-[56px] items-center">
			<div class="flex flex-col gap-[38px]">
				<div class="font-manrope text-[16px] leading-[20.8px] tracking-[2%]">
					В основу базовых услуг Инжинирингового центра новых технологий включены три ключевых направления: веб-дизайн и
					разработка сайтов, графический дизайн и кейтеринг. Концептуальный научных подход к выполнению каждой задачи -
					наше конкурентное преимущество.
				</div>
				<div class="flex gap-[32px]">
					<div v-for="i in counter" class="text-center">
						<div class="text-[40px] leading-[46.9px] font-bold">{{ i.count }}</div>
						<div class="text-[16px] leading-[20px] p-[4px]">{{ i.text }}</div>
					</div>
				</div>
			</div>
			<ImageComponent :img="AboutImageSecond" width="600px" height="307px" radius="10px" object-fit="cover" class="flex-shrink-0"/>
		</div>
	</div>
</template>