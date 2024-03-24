"use client";

import "./globals.css";
import "@mantine/core/styles.css";
import { ColorSchemeScript, MantineProvider, ScrollArea } from "@mantine/core";
import Header from "./components/Header";
import { AppShell } from "@mantine/core";
import { useDisclosure } from "@mantine/hooks";
import algoliasearch from "algoliasearch";
import { InstantSearch } from "react-instantsearch";
import Filters from "./components/Filters";
import FiltersFooter from "./components/FiltersFooter";

const searchClient = algoliasearch(
  "0NVC6NE905",
  "ef099700e7cf4939581005a45ddcdeec",
);

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const [opened, { toggle }] = useDisclosure();

  return (
    <html lang="en">
      <head>
        <ColorSchemeScript />
      </head>
      <body className="flex flex-col h-screen">
        <MantineProvider
          theme={{
            fontFamily: "Courier, monospace",
            fontFamilyMonospace: "Courier, monospace",
            headings: { fontFamily: "Courier, monospace" },
          }}
        >
          <InstantSearch
            searchClient={searchClient}
            indexName="properties"
            future={{
              preserveSharedStateOnUnmount: true,
            }}
          >
            <AppShell
              header={{ height: { base: 50, md: 60, lg: 70 } }}
              navbar={{
                width: { base: 200, md: 300, lg: 400 },
                breakpoint: "sm",
                collapsed: { mobile: !opened },
              }}
              padding="sm"
            >
              <AppShell.Header className="bg-emerald-700">
                <Header opened={opened} toggle={toggle} />
              </AppShell.Header>
              <AppShell.Navbar>
                <AppShell.Section
                  grow
                  component={ScrollArea}
                  className="overscroll-none"
                >
                  <Filters />
                </AppShell.Section>
                <AppShell.Section>
                  <FiltersFooter opened={opened} toggle={toggle} />
                </AppShell.Section>
              </AppShell.Navbar>
              <AppShell.Main>{children}</AppShell.Main>
            </AppShell>
          </InstantSearch>
        </MantineProvider>
      </body>
    </html>
  );
}
