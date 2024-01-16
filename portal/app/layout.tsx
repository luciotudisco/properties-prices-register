import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import Footer from "./components/Footer";
import Header from "./components/Header";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Properties Prices Register",
  description: "Properties Prices Register",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="flex flex-col h-screen">
        <header className="min-h-14">
          <Header />
        </header>
        <main className="flex-grow">{children}</main>
        <footer className="min-h-10">
          <Footer />
        </footer>
      </body>
    </html>
  );
}
