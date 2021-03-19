package com.example.helloworldservice.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import java.util.Optional;
@javax.annotation.Generated(value = "org.openapitools.codegen.languages.SpringCodegen", date = "2021-03-16T15:42:06.037381-04:00[America/New_York]")
@Controller
@RequestMapping("${openapi.&quot;Hello World Service&quot;.base-path:}")
public class HelloworldApiController implements HelloworldApi {

    private final HelloworldApiDelegate delegate;

    public HelloworldApiController(@org.springframework.beans.factory.annotation.Autowired(required = false) HelloworldApiDelegate delegate) {
        this.delegate = Optional.ofNullable(delegate).orElse(new HelloworldApiDelegate() {});
    }

    @Override
    public HelloworldApiDelegate getDelegate() {
        return delegate;
    }

}
