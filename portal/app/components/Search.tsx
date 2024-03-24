import { InfiniteHits, useInstantSearch, useStats } from "react-instantsearch";
import SearchHit from "./SearchHit";
import EmptyHits from "./EmptyHits";
import SearchCurrentRefinements from "./CurrentRefinements";
import SearchGraph from "./SearchGraph";
import { SearchView } from "../types/models";
import { Flex, Tabs, Text } from "@mantine/core";
import { IconChartLine, IconLayoutList } from "@tabler/icons-react";

const Search = function (): JSX.Element {
  const { results } = useInstantSearch();
  const { nbHits } = useStats();

  if (!results.__isArtificial && results.nbHits === 0) {
    return (
      <Flex align="center" justify="center" className="h-full">
        <EmptyHits />
      </Flex>
    );
  }

  return (
    <Tabs variant="pills" defaultValue={SearchView.LIST}>
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
      <Tabs.Panel value={SearchView.LIST} className="mx-5 md:mx-20 xl:mx-40">
        <SearchCurrentRefinements />
        <Text
          className="text-gray-400 mb-2 text-center"
          variant="caption"
          size="xs"
        >
          {nbHits} results found
        </Text>
        <InfiniteHits hitComponent={SearchHit} showPrevious={false} />
      </Tabs.Panel>
      <Tabs.Panel value={SearchView.GRAPH} className="mx-5 md:mx-20 xl:mx-40">
        <SearchCurrentRefinements />
        <SearchGraph />
      </Tabs.Panel>
    </Tabs>
  );
};

export default Search;
