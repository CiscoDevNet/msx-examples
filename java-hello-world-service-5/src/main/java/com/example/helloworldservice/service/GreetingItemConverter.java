//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.service;

import com.example.helloworldservice.cockroach.model.GreetingRow;
import com.example.helloworldservice.model.Item;
import com.example.helloworldservice.model.Language;
import org.springframework.util.Assert;

public class GreetingItemConverter {
    // Convert from domain model into DTO.
    public static Item convert(GreetingRow greeting) {
        Item item = new Item()
                .id(greeting.getGreetingId())
                .languageId(greeting.getLanguage().getLanguageId())
                .languageName(greeting.getLanguage().getName())
                .value(greeting.getValue());
        return item;
    }

    // Convert from DTO into domain model.
    public static GreetingRow convert(Item item, Language language) {
        Assert.notNull(item, "Item is a required field for mapping.");
        Assert.notNull(language, "Language is a required field for mapping.");
        Assert.isTrue(item.getLanguageId().equals(language.getId()), "Mismatch between expected and provided language for given item.");

        GreetingRow.GreetingRowBuilder greetingBuilder = GreetingRow.builder();

        if (item.getId() != null) {
            greetingBuilder.greetingId(item.getId());
        }

        greetingBuilder
                .language(LanguageItemConverter.convert(language))
                .value(item.getValue());

        return greetingBuilder.build();
    }
}