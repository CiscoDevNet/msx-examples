//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.config;

import com.example.helloworldservice.service.ItemsService;
import com.example.helloworldservice.service.LanguagesService;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ServiceConfig {

    @Bean
    public ItemsService itemsService(LanguagesService languageService) {
        return new ItemsService(languageService);
    }

    @Bean
    public LanguagesService languagesService() {
        return new LanguagesService();
    }
}
