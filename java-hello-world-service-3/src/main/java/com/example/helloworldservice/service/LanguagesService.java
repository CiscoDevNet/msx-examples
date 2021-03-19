//
// Copyright (c) 2021 Cisco Systems, Inc and its affiliates
// All Rights reserved
//
package com.example.helloworldservice.service;

import com.example.helloworldservice.model.Language;
import lombok.RequiredArgsConstructor;

import java.util.Arrays;
import java.util.List;
import java.util.UUID;

@RequiredArgsConstructor
public class LanguagesService {
    // Mock resources.
    private static final Language MOCK_LANGUAGE = new Language()
            .id(UUID.randomUUID())
            .name("English")
            .description("A West Germanic language that uses the Roman alphabet.");

    public Language saveLanguage(Language language) {
        return MOCK_LANGUAGE;
    }

    public Language getLanguage(UUID languageId) {
        return MOCK_LANGUAGE;
    }

    public List<Language> getAllLanguages() {
        return Arrays.asList(MOCK_LANGUAGE);
    }

    public Language updateLanguage(UUID languageId, Language language) {
        return MOCK_LANGUAGE;
    }

    public void deleteLanguage(UUID languageId) {
    }
}