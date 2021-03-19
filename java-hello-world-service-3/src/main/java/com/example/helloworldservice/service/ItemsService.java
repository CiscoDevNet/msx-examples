//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.service;

import com.example.helloworldservice.model.Item;
import lombok.RequiredArgsConstructor;

import java.util.Arrays;
import java.util.List;
import java.util.UUID;


@RequiredArgsConstructor
public class ItemsService {
    private final LanguagesService languageService;

    // Mock resources.
    private static final Item MOCK_ITEM = new Item()
            .id(UUID.randomUUID())
            .languageId(UUID.randomUUID())
            .languageName("English")
            .value("Hello, World!");

    public Item saveGreeting(Item item) {
        return MOCK_ITEM;
    }

    public Item getGreeting(UUID greetingId) {
        return MOCK_ITEM;
    }

    public List<Item> getAllGreetingsByLanguage(UUID languageId) {
        return Arrays.asList(MOCK_ITEM);
    }

    public Item updateGreeting(UUID greetingId, Item item) {
        return MOCK_ITEM;
    }

    public void deleteGreeting(UUID greetingId) {
    }
}