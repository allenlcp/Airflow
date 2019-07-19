package com.example.demo;

import lombok.Data;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Profile;
import org.springframework.stereotype.Component;

@Component
@Profile("printer")
@Data
public class Printer {
    @Value("${home.config.url}")
    private String url;

    @Value("${home.config.port}")
    private String port;

    @Value("${kafka.config.topic}")
    private String topic;

    @Autowired
    private ApplicationConfig config;

    @Override
    public String toString() {
        return "Printer{" +
                "url='" + url + '\'' +
                ", port='" + port + '\'' +
                ", username='" + config.getAppconfig().getUsername() + '\'' +
                ", topic='" + topic + '\'' +
                ", instrument='" + config.getAppconfig().getInstrument() + '\'' +
                '}';
    }
}
