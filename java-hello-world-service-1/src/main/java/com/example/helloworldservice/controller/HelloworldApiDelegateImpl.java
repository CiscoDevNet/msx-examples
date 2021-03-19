//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.controller;

import com.example.helloworldservice.model.Item;
import com.example.helloworldservice.model.Language;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import java.util.Arrays;
import java.util.List;
import java.util.UUID;

/**
 * Implementation of service delegate for language and greeting items.
 */
@RequiredArgsConstructor
public class HelloworldApiDelegateImpl implements HelloworldApiDelegate {
    // Mock resources.
    private static final Language MOCK_LANGUAGE = new Language()
            .id(UUID.randomUUID())
            .name("English");

    private static final Item MOCK_ITEM = new Item()
            .id(UUID.randomUUID())
            .languageId(UUID.randomUUID())
            .languageName("English")
            .value("Hello, World!");

    // Languages
    @Override
    public ResponseEntity<Language> createLanguage(Language language) {
        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(MOCK_LANGUAGE);
    }

    @Override
    public ResponseEntity<Language> getLanguage(UUID id) {
        return ResponseEntity.ok(MOCK_LANGUAGE);
    }

    @Override
    public ResponseEntity<List<Language>> getLanguages() {
        return ResponseEntity.ok(Arrays.asList(MOCK_LANGUAGE));
    }

    @Override
    public ResponseEntity<Language> updateLanguage(UUID id, Language language) {
        return ResponseEntity.ok(MOCK_LANGUAGE);
    }

    @Override
    public ResponseEntity<Void> deleteLanguage(UUID id) {
        return ResponseEntity.noContent().build();
    }

    // Items
    @Override
    public ResponseEntity<Item> createItem(Item item) {
        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(MOCK_ITEM);
    }

    @Override
    public ResponseEntity<Item> getItem(UUID id) {
        return ResponseEntity.ok(MOCK_ITEM);
    }

    @Override
    public ResponseEntity<List<Item>> getItems(UUID languageId) {
        return ResponseEntity.ok(Arrays.asList(MOCK_ITEM));
    }

    @Override
    public ResponseEntity<Void> deleteItem(UUID id) {
        return ResponseEntity.noContent().build();
    }

    @Override
    public ResponseEntity<Item> updateItem(UUID id, Item item) {
        return ResponseEntity.ok(MOCK_ITEM);
    }
}