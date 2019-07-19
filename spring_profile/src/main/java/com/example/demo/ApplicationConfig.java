package com.example.demo;

import lombok.Data;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Configuration;

@Configuration
@ConfigurationProperties("app.config")
@Data
public class ApplicationConfig {
    FactoryConfig appconfig = new FactoryConfig();
}
