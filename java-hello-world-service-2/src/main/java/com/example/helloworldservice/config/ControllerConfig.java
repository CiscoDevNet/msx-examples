//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.config;

import com.example.helloworldservice.controller.HelloworldApiDelegate;
import com.example.helloworldservice.controller.HelloworldApiDelegateImpl;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class ControllerConfig {
    @Bean
    public HelloworldApiDelegate helloworldApiDelegate() {
        return new HelloworldApiDelegateImpl();
    }
}