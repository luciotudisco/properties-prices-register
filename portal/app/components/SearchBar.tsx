import { useSearchBox } from "react-instantsearch";
import "instantsearch.css/themes/satellite.css";
import { CloseButton, Input } from "@mantine/core";
import { useEffect, useState } from "react";
import { IconSearch } from "@tabler/icons-react";

const SearchBar = function (): JSX.Element {
  const { query, refine } = useSearchBox();
  const [value, setValue] = useState(query);

  useEffect(() => {
    setValue(query);
  }, [query]);

  return (
    <Input
      placeholder="Search property"
      value={value}
      onChange={(event) => {
        refine(event.currentTarget.value);
      }}
      className="max-w-lg w-full"
      leftSection={<IconSearch size={16} />}
      rightSectionPointerEvents="all"
      rightSection={
        <CloseButton
          aria-label="Clear input"
          onClick={() => refine("")}
          style={{ display: value ? undefined : "none" }}
        />
      }
    />
  );
};

export default SearchBar;
