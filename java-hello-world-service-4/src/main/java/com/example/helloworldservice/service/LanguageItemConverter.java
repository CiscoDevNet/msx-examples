//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.service;

import com.example.helloworldservice.cockroach.model.LanguageRow;
import com.example.helloworldservice.model.Language;

public class LanguageItemConverter {
    // Convert from domain model into DTO.
    public static Language convert(LanguageRow languageRow) {
        Language language = new Language()
                .id(languageRow.getLanguageId())
                .name(languageRow.getName())
                .description(languageRow.getDescription());
        return language;
    }

    // Convert from DTO into domain model.
    public static LanguageRow convert(Language language) {
        LanguageRow languageRow = LanguageRow.builder()
                .languageId(language.getId())
                .name(language.getName())
                .description(language.getDescription())
                .build();
        return languageRow;
    }
}