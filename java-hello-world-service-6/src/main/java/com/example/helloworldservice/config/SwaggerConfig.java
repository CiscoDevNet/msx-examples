//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.config;

import com.cisco.msx.swagger.SwaggerConfigurer;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.spring.web.plugins.Docket;

import java.util.function.Predicate;

import static springfox.documentation.builders.PathSelectors.regex;

@Configuration
public class SwaggerConfig implements SwaggerConfigurer {

    @Value("${info.app.name}")
    private String appName;

    @Value("${info.app.description}")
    private String appDescription;

    @Value("${info.app.version}")
    private String appVersion;

    @Value("${info.app.attributes.parent:platform}")
    private String componentGroup;

    @Value("${server.servlet.context-path}")
    private String contextPath;

    @Override
    public Docket configure(Docket docket) {
        return docket.groupName(componentGroup);
    }

    @Override
    public ApiInfoBuilder configureApiInfo(ApiInfoBuilder apiInfo) {

        return apiInfo
                .title("MSX API Documentation for " + appName)
                .description(appDescription)
                .version(appVersion);
    }

    public Predicate<String> configureApiPathSelector(Predicate<String> apiPathSelector) {
        return apiPathSelector.or(regex(contextPath + "/helloworld/api/v1.*"));
    }
}
