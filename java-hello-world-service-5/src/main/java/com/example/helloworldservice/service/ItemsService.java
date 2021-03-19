//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.service;

import com.example.helloworldservice.cockroach.model.GreetingRow;
import com.example.helloworldservice.cockroach.model.LanguageRow;
import com.example.helloworldservice.cockroach.repository.GreetingsRepository;
import com.example.helloworldservice.model.Item;
import com.example.helloworldservice.model.Language;

import java.util.List;
import java.util.UUID;
import java.util.stream.Collectors;

import lombok.RequiredArgsConstructor;

@RequiredArgsConstructor
public class ItemsService {
    private final GreetingsRepository greetingsRepository;

    private final LanguagesService languagesService;

    public Item saveGreeting(Item item) {
        // Convert the DTO into the domain model.
        Language language = languagesService.getLanguage(item.getLanguageId());
        GreetingRow greetingRow = GreetingItemConverter.convert(item, language);

        // Save domain model object.
        GreetingRow savedGreetingRow = greetingsRepository.save(greetingRow);

        // Convert domain model to DTO in preparation for response.
        Item savedItem = GreetingItemConverter.convert(savedGreetingRow);

        return savedItem;
    }

    public Item getGreeting(UUID greetingId) {
        // Obtain greeting record from database.
        GreetingRow greeting = greetingsRepository.getOne(greetingId);

        // Convert domain model to DTO for response.
        Item item = GreetingItemConverter.convert(greeting);

        return item;
    }

    public List<Item> getAllGreetings() {
        // Obtain records from database.
        List<GreetingRow> greetingRows = greetingsRepository.findAll();

        // Convert records into DTOs.
        List<Item> languages = greetingRows.stream()
                .map(GreetingItemConverter::convert)
                .collect(Collectors.toList());

        return languages;
    }

    public List<Item> getAllGreetingsByLanguage(UUID languageId) {
        // Obtain language.
        LanguageRow language = null;
        if (languageId != null) {
            language = languagesService.getRawLanguage(languageId);
        }

        // Obtain records from database.
        List<GreetingRow> greetingRows = greetingsRepository.findAllByLanguage(language);

        // Convert records into DTOs.
        List<Item> languages = greetingRows.stream()
                .map(GreetingItemConverter::convert)
                .collect(Collectors.toList());

        return languages;
    }

    public Item updateGreeting(UUID greetingId, Item item) {
        // Will throw exception if greeting entry does not exist.
        GreetingRow existingGreetingRow = greetingsRepository.getOne(greetingId);

        // Convert the DTO into the domain model.
        Language language = languagesService.getLanguage(item.getLanguageId());
        GreetingRow greetingRow = GreetingItemConverter.convert(item, language);

        // Set greetingId to overwrite existing record.
        greetingRow.setGreetingId(greetingId);

        // Save domain model object.
        GreetingRow savedGreetingRow = greetingsRepository.save(greetingRow);

        // Convert domain model to DTO in preparation for response
        Item savedItem = GreetingItemConverter.convert(savedGreetingRow);

        return savedItem;
    }

    public void deleteGreeting(UUID greetingId) {
        greetingsRepository.deleteById(greetingId);
    }
}