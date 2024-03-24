import { useInstantSearch } from "react-instantsearch";
import Hits from "./Hits";
import EmptyHits from "./EmptyHits";
import Refinements from "./Refinements";
import Graph from "./Graph";
import { SearchView } from "../types/models";
import { Flex, Loader, LoadingOverlay, Tabs } from "@mantine/core";
import { IconChartLine, IconLayoutList } from "@tabler/icons-react";

const Search = function (): JSX.Element {
  const { results, status } = useInstantSearch();

  if (status === "loading") {
    return (
      <Flex className="flex h-svh w-full justify-center items-center">
        <Loader />
      </Flex>
    );
  }

  if (!results.__isArtificial && results.nbHits === 0) {
    return (
      <Flex className="flex h-svh w-full justify-center items-center">
        <EmptyHits />
      </Flex>
    );
  }

  return (
    <Tabs
      variant="pills"
      defaultValue={SearchView.LIST}
      className="mx-5 md:mx-10 xl:mx-40"
    >
      <Tabs.List className="justify-end">
        <Tabs.Tab
          value={SearchView.LIST}
          leftSection={<IconLayoutList size={16} />}
        >
          List
        </Tabs.Tab>
        <Tabs.Tab
          value={SearchView.GRAPH}
          leftSection={<IconChartLine size={16} />}
        >
          Graph
        </Tabs.Tab>
      </Tabs.List>
      <Tabs.Panel value={SearchView.LIST}>
        <Refinements />
        <Hits />
      </Tabs.Panel>
      <Tabs.Panel value={SearchView.GRAPH}>
        <Refinements />
        <Graph />
      </Tabs.Panel>
    </Tabs>
  );
};

export default Search;
