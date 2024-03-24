import SearchBar from "./SearchBar";
import { Burger, Flex, Title } from "@mantine/core";

export interface HeaderProps {
  opened?: boolean;
  toggle: () => void;
}

const Header = function (props: HeaderProps): JSX.Element {
  const { opened, toggle } = props;
  return (
    <Flex direction="row" align="center" gap="sm" className="w-full">
      <Burger opened={opened} onClick={toggle} hiddenFrom="sm" size="sm" />
      <Title order={1} className="w-full text-sm md:text-xl">
        Irish Properties Prices
      </Title>
      <SearchBar />
    </Flex>
  );
};

export default Header;
