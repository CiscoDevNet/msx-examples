//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.controller;

import com.example.helloworldservice.model.Item;
import com.example.helloworldservice.model.Language;
import com.example.helloworldservice.service.ItemsService;
import com.example.helloworldservice.service.LanguagesService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import java.util.List;
import java.util.UUID;

@RequiredArgsConstructor
public class HelloworldApiDelegateImpl implements HelloworldApiDelegate {
    private final ItemsService itemsService;

    private final LanguagesService languagesService;

    // Languages
    @Override
    public ResponseEntity<Language> createLanguage(Language language) {
        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(languagesService.saveLanguage(language));
    }

    @Override
    public ResponseEntity<Language> getLanguage(UUID id) {
        return ResponseEntity.ok(languagesService.getLanguage(id));
    }

    @Override
    public ResponseEntity<List<Language>> getLanguages() {
        return ResponseEntity.ok(languagesService.getAllLanguages());
    }

    @Override
    public ResponseEntity<Language> updateLanguage(UUID id, Language language) {
        return ResponseEntity.ok(languagesService.updateLanguage(id, language));
    }

    @Override
    public ResponseEntity<Void> deleteLanguage(UUID id) {
        languagesService.deleteLanguage(id);
        return ResponseEntity.noContent().build();
    }

    // Items
    @Override
    public ResponseEntity<Item> createItem(Item item) {
        return ResponseEntity
                .status(HttpStatus.CREATED)
                .body(itemsService.saveGreeting(item));
    }

    @Override
    public ResponseEntity<Item> getItem(UUID id) {
        return ResponseEntity.ok(itemsService.getGreeting(id));
    }

    @Override
    public ResponseEntity<List<Item>> getItems(UUID languageId) {
        return ResponseEntity.ok(itemsService.getAllGreetingsByLanguage(languageId));
    }

    @Override
    public ResponseEntity<Item> updateItem(UUID id, Item item) {
        return ResponseEntity.ok(itemsService.updateGreeting(id, item));
    }

    @Override
    public ResponseEntity<Void> deleteItem(UUID id) {
        itemsService.deleteGreeting(id);
        return ResponseEntity.noContent().build();
    }
}