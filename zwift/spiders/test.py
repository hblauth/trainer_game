# -*- coding: utf-8 -*-
import scrapy


class TestSpider(scrapy.Spider):
    name = 'test'

    start_urls = [
        'https://whatsonzwift.com/workouts/build-me-up/#build-me-up']

    def parse(self, response):
        workouts = response.css('.workout')

        for workout in workouts:
            yield {
                'week_name': workout.css('a::text').getall()[1],
                'workout_name2': workout.css('.glyph-icon.flaticon-bike::text').getall(),
                'workout_length': workout.css('.three.columns p::text').getall()[0],
                'stress_points': workout.css('.three.columns p::text').getall()[1]
            }
